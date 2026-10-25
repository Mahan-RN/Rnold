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
                <nav className={styles.pages}>
                    <NavLink
                        to="/"
                        end
                        className={({ isActive }) =>
                            isActive
                                ? `${styles.navLink} ${styles.active}`
                                : styles.navLink
                        }
                    >
                        Home
                    </NavLink>
                    <NavLink
                        to="/about"
                        className={({ isActive }) =>
                            isActive
                                ? `${styles.navLink} ${styles.active}`
                                : styles.navLink
                        }
                    >
                        About
                    </NavLink>
                </nav>
                <div className={styles.login}>
                    {user !== undefined && user !== null && user.role === 2 && (
                        <NavLink
                            to="/admin"
                            end
                            className={({ isActive }) =>
                                isActive
                                    ? `${styles.navLink} ${styles.active}`
                                    : styles.navLink
                            }
                        >
                            Admin Dashboard
                        </NavLink>
                    )}
                    {user !== undefined && user !== null ? (
                        <span>{user.username}</span>
                    ) : (
                        <NavLink
                            to="/login"
                            className={({ isActive }) =>
                                isActive
                                    ? `${styles.navLink} ${styles.active}`
                                    : styles.navLink
                            }
                        >
                            Log in
                        </NavLink>
                    )}
                </div>
            </div>
        </header>
    );
}
