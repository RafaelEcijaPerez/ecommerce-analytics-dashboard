const API_URL = "http://127.0.0.1:8000";

export const getRevenueSummary = async () => {
  const res = await fetch(`${API_URL}/sales/revenue-summary`);
  return res.json();
};

export const getTopProducts = async () => {
  const res = await fetch(`${API_URL}/sales/top-products`);
  return res.json();
};