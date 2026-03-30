const API_URL = "http://127.0.0.1:8000";

export const getRevenueSummary = async () => {
  const res = await fetch(`${API_URL}/sales/revenue-summary`);
  return res.json();
};

export const getTopProducts = async () => {
  const res = await fetch(`${API_URL}/sales/top-products`);
  return res.json();
};

export const getCustomers = async () => {
  const res = await fetch(`${API_URL}/customers`);
  return res.json();
}
export const getProducts = async () => {
  const res = await fetch(`${API_URL}/products`);
  return res.json();
}
export const getSales = async () => {
  const res = await fetch(`${API_URL}/sales`);
  return res.json();
};
export const getSalesByDateRange = async (start, end) => {
  const res = await fetch(`${API_URL}/sales/date-range?start_date=${start}&end_date=${end}`);
  return res.json();
};