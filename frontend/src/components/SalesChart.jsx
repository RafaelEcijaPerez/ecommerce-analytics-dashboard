import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  ResponsiveContainer,
  CartesianGrid
} from "recharts";

function SalesChart({ data }) {
  return (
    <div style={{
      width: "100%",
      height: 300,
      background: "#fff",
      padding: "20px",
      borderRadius: "12px",
      boxShadow: "0 2px 8px rgba(33, 187, 234, 0.1)"
    }}>
      <ResponsiveContainer>
        <BarChart data={data}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="product_name" />
          <YAxis />
          <Tooltip />
          <Bar dataKey="total_sold" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}

export default SalesChart;