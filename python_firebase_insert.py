"""
Prequisets:
1. pip install requests
2. pip install python-firebase
>>Create an project in firebase
"""


from firebase import firebase


"""This will make the connection to firebase DB file"""
firebase =  firebase.FirebaseApplication("https://learn-python-firebase-dc967.firebaseio.com/", None)

"""Data that you eant to send to firebase table"""
data_document = {
    'Name': 'John Wick',
    'Location': 'New York',
    'Killed' : 211
}

"""Using POst method you can send to cloud firebase"""
result = firebase.post("/learn-python-firebase-dc967/MyFuckingTable", data_document)
print(result)