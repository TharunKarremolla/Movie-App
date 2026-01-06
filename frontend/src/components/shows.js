import { useState, useEffect } from "react";
import axios from 'axios';
import { useParams } from "react-router-dom";
import { useNavigate, useLocation} from "react-router-dom";

export default function Shows(){
    const API_URL = process.env.REACT_APP_API_URL;
    const [title,setTitle] = useState(null);
    const { movieId } = useParams();
    const [timings,setTimings] = useState()
    const [data,setData] = useState([])
    const navigate = useNavigate()
     
    
const getTheaters = async() => {
  const res = await axios.get(`${API_URL}shows/movies/${movieId}/theaters/`,)
    setData(res.data.data)
    setTimings(res.data.timings)
    setTitle(res.data.title)
    }
    useEffect(()=>{
        getTheaters()
    },[movieId])
    return (
        <div>
        <h1>{title}</h1>
      {timings && Object.entries(timings).map(([key,values])=>(
        <div key={key}>
            <h3 >{key}</h3>

                {values.map((value,index)=>(
                    <p key={index} 
                    style={{listStyleType : "none"}} >
                 <button onClick={() => navigate("/billing",{ state : {"price" : value.price,"show" : value.time,"title" : title,'theater' : key,'show_id' : value.id}})}>{value.time}</button>
                    </p>
                ))}
            </div>
      ) )
    }
 

  </div> )
}
