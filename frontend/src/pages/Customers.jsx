import { useEffect, useState } from "react";
import { getCustomers } from "../services/api";

function Customers() {
  const [customers, setCustomers] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      const res = await getCustomers();
      setCustomers(res.data);
      setLoading(false);
    };

    fetchData();
  }, []);

  if (loading) return <p>Cargando...</p>;

  return (
    <div>
      <h1 style={{ textAlign: "center" }}>👤 Customers</h1>

      <table style={{
        width: "100%",
        borderCollapse: "collapse",
        marginTop: "20px"
      }}>        
      <thead>
          <tr style={{ background: "#ddd"}}>
            <th>Name</th>
            <th>Email</th>
          </tr>
        </thead>
        <tbody>
          {customers.map((cust) => (
            <tr key={cust.id} style={{textAlign :"center"}}>
              <td>{cust.name}</td>
              <td>{cust.email}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Customers;