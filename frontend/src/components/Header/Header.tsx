import { Link, NavLink, useRouteLoaderData } from "react-router";
import type { CurrentUser } from "src/loaders/RootLayoutLoader";
import logo from "src/assets/logo.svg";
import styles from "src/components/Header/Header.module.css";

export default function Header() {
    const user = useRouteLoaderData<CurrentUser | null>("root");
    return (
        <header className={styles.rootHeader}>
            <Link to="/" className={styles.rootLogo}>
                <img src={logo} alt="Rnold home" />
            </Link>
            <div className={styles.navigationBar}>
                <nav>
                    <NavLink to="/" end>
                        Home
                    </NavLink>
                    <NavLink to="/about">About</NavLink>
                </nav>
                <div className={styles.login}>
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
            </div>
        </header>
    );
}
