import Navbar from "./Navbar";

function Layout({ children }) {
  return (
    <div style={{ display: "flex" }}>
      <Navbar />
      <div style={{
        padding: "20px",
        width: "100%"
      }}>
        {children}
      </div>
    </div>
  );
}

export default Layout;