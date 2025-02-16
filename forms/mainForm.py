# import sys
# import os
import curses
import curses.textpad
from models.LeadModel import LeadModel
from models.OrganizationModel import OrganizationModel
from models.ContactModel import ContactModel


def main(stdscr):
    curses.curs_set(1)  # Exibe o cursor para entrada do usuário
    stdscr.clear()

    fields = [
        ("Lead - Nome", "name"),
        ("Lead - Telefone", "phone"),
        ("Lead - Endereço", "address"),
        ("Lead - Cidade", "city"),
        ("Lead - Estado", "state"),
        ("Lead - País", "country"),
        ("Lead - CPF/CNPJ", "cpfCnpj"),
        ("Empresa - Nome", "org_name"),
        ("Empresa - E-mail", "org_email"),
        ("Contato - Nome", "contact_name"),
        ("Contato - E-mail", "contact_email"),
        ("Contato - Telefone", "contact_phone"),
    ]

    values = {field[1]: "" for field in fields}

    current_field = 0
    while current_field < len(fields):
        stdscr.clear()
        stdscr.addstr(0, 0, "Preencha os dados abaixo:")
        for idx, (label, key) in enumerate(fields):
            stdscr.addstr(idx + 2, 0, f"{label}: {values[key]}")

        stdscr.move(current_field + 2, len(fields[current_field][0]) + 2)
        values[fields[current_field][1]] = stdscr.getstr().decode('utf-8').strip()
        current_field += 1

    # Criando os objetos com os valores preenchidos
    lead = LeadModel(name=values["name"], phone=values["phone"], address=values["address"],
                city=values["city"], state=values["state"], country=values["country"],
                cpfCnpj=values["cpfCnpj"])

    organization = OrganizationModel(
        name=values["org_name"], userEmail=values["org_email"], cpfCnpj=values["cpfCnpj"])

    contact = ContactModel(name=values["contact_name"], email=values["contact_email"], phone=values["contact_phone"],
                      leadId=None)  # leadId será definido após a criação do lead

    return lead, organization, contact


if __name__ == "__main__": 
    curses.wrapper(main)
