function Card({ title, value }) {
  return (
    <div style={{
      border: "1px solid #ccc",
      borderRadius: "10px",
      padding: "20px",
      width: "200px"
    }}>
      <h3>{title}</h3>
      <p style={{ fontSize: "20px", fontWeight: "bold" }}>
        {value}
      </p>
    </div>
  );
}

export default Card;