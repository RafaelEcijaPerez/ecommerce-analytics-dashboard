import { useEffect, useState } from "react";
import { getSales, getSalesByDateRange } from "../services/api";

function Sales() {
  const [sales, setSales] = useState([]);
  const [loading, setLoading] = useState(true);
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");
  const [filtering, setFiltering] = useState(false);

  useEffect(() => {
    const timeout = setTimeout(() => {
      const fetchData = async () => {
        // 👇 solo loading la primera vez
        if (loading) setLoading(true);
        else setFiltering(true);

        try {
          let res;

          if (startDate && endDate) {
            res = await getSalesByDateRange(startDate, endDate);
          } else {
            res = await getSales();
          }

          setSales(res.data);
        } catch (error) {
          console.error("Error fetching sales:", error);
        }

        setLoading(false);
        setFiltering(false);
      };

      fetchData();
    }, 500); // debounce

    return () => clearTimeout(timeout);
  }, [startDate, endDate]);

  if (loading) return <p>Cargando...</p>;

  return (
    <div>
      <h1>💰 Sales</h1>

      <div style={{
        marginBottom: "20px",
        display: "flex",
        gap: "10px",
        justifyContent: "center"
      }}>
        <input
          type="date"
          value={startDate}
          onChange={(e) => setStartDate(e.target.value)}
        />

        <input
          type="date"
          value={endDate}
          onChange={(e) => setEndDate(e.target.value)}
        />
      </div>

      {filtering && <p>Filtrando datos...</p>}

      <table
        style={{
          width: "100%",
          borderCollapse: "collapse",
          marginTop: "20px",
        }}
      >
        <thead>
          <tr style={{ background: "#ddd" }}>
            <th>ID</th>
            <th>Customer</th>
            <th>Product</th>
            <th>Date</th>
            <th>Revenue</th>
          </tr>
        </thead>

        <tbody>
          {sales.map((sale) => (
            <tr key={sale.id} style={{ textAlign: "center" }}>
              <td>{sale.id}</td>
              <td>{sale.customer_name}</td>
              <td>{sale.product_name}</td>
              <td>{sale.date}</td>
              <td>{sale.revenue.toFixed(2)} €</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Sales;