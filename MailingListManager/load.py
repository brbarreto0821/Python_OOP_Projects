# Loading the database that was save in the cell above
m = MailingList('addresses.db')
print(m.email_map)
m.load()
m.email_map