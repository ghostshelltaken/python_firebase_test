from firebase import firebase

firebase =  firebase.FirebaseApplication("https://learn-python-firebase-dc967.firebaseio.com/", None) 

firebase.delete("/learn-python-firebase-dc967/MyFuckingTable/", '-M49iqGqaw3e-H0PFH_I')
print("Recoed deleted!")