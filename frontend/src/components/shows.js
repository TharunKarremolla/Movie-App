import { useState, useEffect } from "react";
import axios from 'axios';
import { useParams } from "react-router-dom";
import { useNavigate, useLocation} from "react-router-dom";
import Cookies from 'js-cookie';
export default function Shows(){
    const API_URL = process.env.REACT_APP_API_URL;
    const [title,setTitle] = useState(null);
    const { movieId } = useParams();
    const [tickets,setTickets] = useState(0)
    const [timings,setTimings] = useState()
    const [data,setData] = useState([])
    const navigate = useNavigate()
    const [selectedShow, setSelectedShow] = useState(null);
    
    const getTickets = async() =>{
  const res = await axios.post(`${API_URL}bookings/`,{show : selectedShow ,total_tickets : tickets},{
    withCredentials : true,
    headers : {
      "Content-Type" :  "application/json",
        'X-CSRFToken' : Cookies.get('csrftoken')
    }
  })
 console.log(res.data)
  navigate(`/bookings/`)
}   
    
    const getTheaters = async() => {
  const res = await axios.get(`${API_URL}shows/movies/${movieId}/theaters/`,)
    setData(res.data.data)
    setTimings(res.data.timings)
    setTitle(res.data.title)
// console.log(res.data.title)
    }
    useEffect(()=>{
        getTheaters()
    },[])
    return (
        <div>
        <h1>{title}</h1>
      {timings && Object.entries(timings).map(([key,values])=>(
        <div key={key}>
            <h3 >{key}</h3>
            <ul>
                {values.map((value,index)=>(
                    <li key={index} style={{listStyleType : "none"}} >
                        <button onClick={() => setSelectedShow(value)} 
                        style={{
                  cursor: "pointer",
                  padding: "8px",
                  marginBottom: "6px",
                  border: "1px solid #ccc",
                  borderRadius : "5px",
                  color: selectedShow === value ? "white" : 'black',
                  backgroundColor:
                    selectedShow === value ? "red" : "transparent"
                }}  >{value}</button>
                    </li>
                ))}
            </ul>

            </div>
      ))
    }
     <label>Number of tickets</label>
        
        <input type="text" onChange={(e) => setTickets(e.target.value)} />
        

        <button onClick={getTickets}>Book tickets</button>

  </div>)
}
   