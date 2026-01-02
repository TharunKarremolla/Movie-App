import { useState, useEffect } from "react";
import axios from 'axios';
import Cookies from 'js-cookie';
import { useNavigate } from "react-router-dom";
import styles from './Register.module.css';
import { Link } from "react-router-dom";


axios.defaults.withCredentials = true; 


export default function Register({ children }){
    const API_URL = process.env.REACT_APP_API_URL
    const [username,setUsername] = useState('')
    const [password,setPassword] = useState('')
    const [email,setEmail] = useState('')
    const [valid_name,setName] = useState('')
    const [valid_email,setValidEmail] = useState('')
    const [valid_password,setValidPassword] = useState('')
   
    const navigate = useNavigate();
    

    const handSubmit = async () => {
        try {
        const res = await axios.post(`${API_URL}auth/register/`,
            {username,email,password},
            {
                withCredentials : true,
                headers : {
                   "X-CSRFToken" : Cookies.get('csrftoken')
                                    }
            }
        )
         navigate("/Login")
    }
    catch(error){
        console.log("error occurred : ",error)
    }
    }

     const getCsrf = async () => {
        try {
        const res = await axios.get(`${API_URL}auth/`)     
       
    }
    catch(error){
        console.log("error occurred : ",error)  
    }
    }

    useEffect(()=> {
        getCsrf();
},[])

  


    return (
        <div className={styles.accDiv}>
            {children }
            <div style={{ width : '100%'}}>
                <h2>Create Account</h2>
                <input  style={{'marginBottom' : valid_name ? '10px' : '20px'}} className={styles.inputs} type="text" placeholder="username" value={username}  onChange={(e) => setUsername(e.target.value) }/>
                { valid_name && <span style={{'color' : 'red'}}>{valid_name}</span>}<br/>
                <input style={{'marginBottom' : valid_email ? '10px' : '20px'}}  className={styles.inputs} type="email" placeholder="email" value={email}  onChange={(e) => setEmail(e.target.value) } /><br></br>
               { valid_email && <span style={{'color' : 'red'}}>{valid_email}</span>}
                <input  style={{'marginBottom' : valid_password ? '10px' : '20px'}} className={styles.inputs} type="password" placeholder="password"  value={password}  onChange={(e) => setPassword(e.target.value) } /><br></br>
                { valid_password && <span style={{'color' : 'red','marginBottom' : '100px'}}>{valid_password}</span>}
               
               
        
                <button className={styles.submitBtn} onClick={handSubmit} disabled={!username || !email || !password}>Submit</button>
                <br></br><br></br><span>Already have an Account? </span>&nbsp;<Link to="/Login">Sign In</Link>
            </div>
        
       
        </div>
    )
}