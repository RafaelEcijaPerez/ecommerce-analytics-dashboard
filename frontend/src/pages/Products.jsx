import { useEffect, useState } from "react";
import { getProducts } from "../services/api";

function Products() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState("");

  useEffect(() => {
    const fetchData = async () => {
      const res = await getProducts();
      setProducts(res.data);
      setLoading(false);
    };

    fetchData();
  }, []);

  if (loading) return <p>Cargando...</p>;
  const filteredProducts = products.filter((prod) =>
    prod.name?.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div>
      <h1 style={{ textAlign: "center" }}>📦 Products</h1>
      <input
        type="text"
        placeholder="Buscar producto..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        style={{
          padding: "8px",
          marginBottom: "20px",
          width: "100%"
        }}
      />

      <table style={{
        width: "100%",
        borderCollapse: "collapse",
        marginTop: "20px"
      }}>
        <thead>
          <tr style={{ background: "#ddd" }}>
            <th>Name</th>
            <th>Price</th>
          </tr>
        </thead>

        <tbody>
          {filteredProducts.map((prod) => (
            <tr key={prod.id} style={{ textAlign: "center" }}>
              <td>{prod.name}</td>
              <td>{prod.price.toFixed(2)} €</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Products;