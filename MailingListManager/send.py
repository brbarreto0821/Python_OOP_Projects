# Using with statement to save and close files
with MailingList('addresses.db') as ml:
    ml.add_to_group('friend3@example.com', 'friends')
    ml.send_mailing("What's up", "hey friends, how's it going", 
                   'me@example.com', 'friends')