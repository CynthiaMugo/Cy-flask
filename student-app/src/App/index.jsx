import { BrowserRouter, Route, Routes } from 'react-router-dom';

function App() {
    return <BrowserRouter>
        <Routes>
            <Route path="/" element={<div className="bg-red-500 text-white p-4">Hello World</div>} />
        </Routes>
    </BrowserRouter>
}