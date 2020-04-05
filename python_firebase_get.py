from firebase import firebase

"""This will make the connection to firebase DB file"""
firebase =  firebase.FirebaseApplication("https://learn-python-firebase-dc967.firebaseio.com/", None)


result = firebase.get("/learn-python-firebase-dc967/MyFuckingTable", '')
print(result)