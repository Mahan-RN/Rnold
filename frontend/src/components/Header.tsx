import { Link, NavLink, useRouteLoaderData } from "react-router";
import type { CurrentUser } from "../loaders/RootLayoutLoader";
import logo from "../assets/logo.svg";

export default function Header() {
    const user = useRouteLoaderData<CurrentUser | null>("root");
    return (
        <header>
            <Link to="/" className="logoLink">
                <img src={logo} alt="Rnold home" />
            </Link>
            <nav>
                <NavLink to="/" end>
                    Home
                </NavLink>
                <NavLink to="/about">About</NavLink>
            </nav>
            <div>
                {user !== undefined && user !== null && user.role === 2 && (
                    <NavLink to="/admin" end>
                        Admin Dashboard
                    </NavLink>
                )}
                {user !== undefined && user !== null ? (
                    <span>{user.username}</span>
                ) : (
                    <NavLink to="/login">Log in</NavLink>
                )}
            </div>
        </header>
    );
}
