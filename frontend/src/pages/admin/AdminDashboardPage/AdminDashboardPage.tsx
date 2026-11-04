import { NavLink, Outlet } from "react-router";

export default function AdminDashboardPage() {
    return (
        <>
            <nav>
                <NavLink to="/admin/users" end>Users</NavLink>
            </nav>
            <Outlet />
        </>
    );
}
