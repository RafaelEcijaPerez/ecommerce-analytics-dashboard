import { useEffect, useState } from "react";
import { getRevenueSummary, getTopProducts } from "../services/api";
import Card from "../components/Card";
import SalesChart from "../components/SalesChart";

function Dashboard() {
    const [data, setData] = useState(null);
    const [topProducts, setTopProducts] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            const res = await getRevenueSummary();
            setData(res.data[0]);
            const top = await getTopProducts();
            setTopProducts(top.data);
        };

        fetchData();
    }, []);

    if (!data) return <p>Cargando dashboard...</p>;
    return (
        <div style={{ padding: "20px", maxWidth: "1000px", margin: "0 auto" }}>
            <h1 style={{ marginBottom: "30px" }}>Dashboard</h1>

            <div style={{
                display: "flex",
                gap: "20px",
                marginBottom: "40px",
                //center cards
                justifyContent: "center"
            }}>
                <Card title="Total Orders" value={data.total_orders} />
                <Card title="Total Revenue" value={data.total_revenue} />
                <Card title="Avg Order Value" value={data.avg_order_value} />
            </div>

            <h2 style={{ textAlign: "center" }}>Top Products</h2>

            <ul style={{ padding: 0 }}>
                {topProducts.map((prod, index) => (
                    <li key={index} style={{
                        listStyle: "none",
                        textAlign: "center",
                        marginBottom: "10px"
                    }}>
                        🛒 {prod.product_name} — {prod.total_sold} ventas
                    </li>
                ))}
            </ul>

            <div style={{ marginTop: "40px" }}>
                <h2 style={{ textAlign: "center" }}>Sales Chart</h2>
                <SalesChart data={topProducts} />
            </div>
        </div>


    );
}

export default Dashboard;