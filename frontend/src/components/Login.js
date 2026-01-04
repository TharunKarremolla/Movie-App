import { useState } from "react";
import axios from 'axios';
import Cookies from 'js-cookie';
import { useNavigate } from "react-router-dom";
import styles from "./Login.module.css";
import { Link } from "react-router-dom";

axios.defaults.withCredentials = true; 

export default function Login({children}){
    const API_URL = process.env.REACT_APP_API_URL
    const [password,setPassword] = useState('')
    const [email,setEmail] = useState('')
    const navigate = useNavigate();
    const [Error,setError] = useState('')
    
    const handleLogin = async ()=>{
   
     
        try {
                const res = await axios.post(`${API_URL}auth/login/`,{'username':email, password},{
                    withCredentials : true,
                    headers : {
                        "Content-Type" : "application/json",
                         "X-CSRFToken": Cookies.get('csrftoken')
                    }
                });
            
                navigate("/Home")
            }
        catch(error){
              setError(error.response.data.error)
            console.log("error : ",error.response.data.error)
        }
    }

    return (
        <div className={styles.logDiv}>
           {children}
           <div className={styles.container}>
                <h1 className={styles.header}>Login</h1>
                <input className={styles.inputs} type="text" placeholder="email or username" value={email}  onChange={(e) => setEmail(e.target.value) }/><br/>
               
                <input className={styles.inputs} type="password" placeholder="password"  value={password}  onChange={(e) => setPassword(e.target.value) } /><br></br>
                   {Error && <p className={styles.error}>{Error}</p>}
                <button className = {styles.submitBtn} onClick={handleLogin}>Sign in</button><br></br><br></br>
                <span>Doesn't have Account ?</span>&nbsp;<Link to="/">Sign Up</Link>
            </div>
        </div>
    )
}