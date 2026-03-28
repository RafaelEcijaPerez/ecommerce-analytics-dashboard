import { NavLink } from "react-router-dom";

function Navbar() {
    return (
        <div style={{
            width: "200px",
            height: "100vh",
            background: "#111",
            color: "#fff",
            padding: "20px",
            display: "flex",
            flexDirection: "column",
            gap: "20px"
        }}>
            <h2>Dashboard</h2>

            <NavLink
                to="/"
                style={({ isActive }) => ({
                    color: "#fff",
                    textDecoration: "none",
                    background: isActive ? "#333" : "transparent",
                    padding: "10px",
                    borderRadius: "8px"
                })}
            >
                🏠 Home
            </NavLink>
            <NavLink to="/sales" style={({ isActive }) => ({
                color: "#fff",
                textDecoration: "none",
                background: isActive ? "#333" : "transparent",
                padding: "10px",
                borderRadius: "8px"
            })}>
                💰 Sales
            </NavLink>
            <NavLink to="/products" style={({ isActive }) => ({
                color: "#fff",
                textDecoration: "none",
                background: isActive ? "#333" : "transparent",
                padding: "10px",
                borderRadius: "8px"
            })}>
                📦 Products
            </NavLink>
            <NavLink to="/customers" style={({ isActive }) => ({
                color: "#fff",
                textDecoration: "none",
                background: isActive ? "#333" : "transparent",
                padding: "10px",
                borderRadius: "8px"
            })}>
                👤 Customers
            </NavLink>
        </div>
    );
}

export default Navbar;