from forms.createForm import lead_data_collect, contact_data_collect
from models.LeadModel import Lead
from models.ContactModel import Contact
from serializers import LeadSerializer, ContactSerializer
from api_requests.crm_api import create_lead, create_contact

# Coletar dados do Lead
dados_lead = coletar_dados_lead()
novo_lead = Lead(**dados_lead)

# Enviar Lead para API e obter leadId real
lead_json = LeadSerializer.serialize(novo_lead)
resposta = create_lead(lead_json)
novo_lead.leadId = resposta["leadId"]

# Coletar e enviar Contato
dados_contato = coletar_dados_contato()
novo_contato = Contact(novo_lead.leadId, **dados_contato)
contato_json = ContactSerializer.serialize(novo_contato)
create_contact(contato_json)
