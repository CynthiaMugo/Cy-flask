import { Outlet } from "react-router-dom";

function MainDash() {
  return (
    <div>
      <h1>Main Dashboard</h1>
      <Outlet />
    </div>
  );
}

export default MainDash;