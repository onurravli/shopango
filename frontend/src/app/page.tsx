"use client";

import { useState, useEffect } from "react";

type Product = {
  id: number;
  name: string;
  desc: string;
  img: string;
  stock: number;
  price: number;
};

export default function Home() {
  const [products, setProducts] = useState([]);
  useEffect(() => {
    fetch("http://127.0.0.1:8000/get_all_products")
      .then((res) => res.json())
      .then((data) => setProducts(data));
  }, []);
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <ul>
        {products.map((product: Product) => {
          return (
            <li key={product.id}>
              <div className="flex flex-col items-center justify-center max-w-lg gap-2">
                <img src={product.img} alt={product.name} className="w-48 h-48" />
                <h2>{product.name}</h2>
                <p className="text-justify">{product.desc}</p>
                <p>Stock: {product.stock}</p>
                <p>Price: ₺{product.price}</p>
              </div>
            </li>
          );
        })}
      </ul>
    </main>
  );
}
