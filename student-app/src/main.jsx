import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import "./index.css"

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <div className="bg-red-500 text-white p-4">Hello World</div>
  </StrictMode>,
)
