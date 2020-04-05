from firebase import firebase

firebase =  firebase.FirebaseApplication("https://learn-python-firebase-dc967.firebaseio.com/", None) 

firebase.put("/learn-python-firebase-dc967/MyFuckingTable/-M49fnytPCZXLwijeMuj", 'Name', 'JOhn Wick Motherfucker')
print("Recoed updated!")