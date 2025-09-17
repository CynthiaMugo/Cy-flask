import { BrowserRouter, Routes, Route } from "react-router-dom";

import Login from './Screens/Login';
import AddStudent from './Screens/Dashboard/Add';
import MainDash from './Screens/Dashboard';
import StudentAnalytics from './Screens/Dashboard/Analytics';
import ListStudent from './Screens/Dashboard/StudentList';



function APP() {
    return <BrowserRouter>
        <Routes>
        <Route path="" element={<Login />}></Route>
        {/* Nested */}
        <Route path="/student" element={<MainDash />}>
          <Route path="" element={<StudentAnalytics />} />
          <Route path="add" element={<AddStudent />} />
          <Route path="list" element={<ListStudent />} />
        </Route>
      </Routes>
    </BrowserRouter>
}

export default APP;