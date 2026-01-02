import { useState, useEffect } from "react";
import axios from 'axios';
import { useNavigate, useLocation} from "react-router-dom";


export default function Shows(){
    const API_URL = process.env.REACT_APP_API_URL;
    const { state } = useLocation();
    const [time,setTime] = useState()
    const [theaters,setTheaters] = useState([])
    const navigate = useNavigate()

    const getTheaters = async() => {
  const res = await axios.get(`${API_URL}shows/`,)
//   setTheaters(res.data.data)
console.log(res.data)
    }
    useEffect(()=>{
        getTheaters()
    },[])
    return (
        <h1>show</h1>
    )
}
   