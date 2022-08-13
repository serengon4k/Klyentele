// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getAuth, createUserWithEmailAndPassword } from "firebase/auth";
import { getFirestore, collection, addDoc } from "firebase/firestore";
import { User } from "@/objects"
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyAq6_HEtoUeiggG1kbKVF_wOnN--UJCToE",
  authDomain: "klyentele.firebaseapp.com",
  projectId: "klyentele",
  storageBucket: "klyentele.appspot.com",
  messagingSenderId: "944242309353",
  appId: "1:944242309353:web:16463ff483e29975a35878"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);

// Export Authentication Funcs
export const auth = getAuth(app)
export const firestore = getFirestore(app)
export const path = ""
export var LicenseKey;

export function CreateUser(auth, password, UserProfile, LicenseKey) {
  UserProfile = new User(UserProfile)
  try {
    createUserWithEmailAndPassword(auth, email, password).then({
        //Create User in LicenseKey Data field
        const Docu = await addDoc(collection(firestore, ""))
      })
  } catch (e) { 

  }
  
  
}
export function SignInUser