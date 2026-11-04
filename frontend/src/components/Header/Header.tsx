import { Link, NavLink, useRouteLoaderData } from "react-router";
import logo from "src/assets/logo.svg";
import styles from "src/components/Header/Header.module.css";
import type rootLayoutLoader from "src/loaders/RootLayoutLoader";
import AuthControls from "../AuthControls/AuthControls";

const ADMIN_ROLE = 2;

export default function Header() {
    const user = useRouteLoaderData<typeof rootLayoutLoader>("root");
    return (
        <header className={styles.rootHeader}>
            <div className={styles.gridContainer}>
                <div className={styles.gridItem1}>
                    <Link to="/" className={styles.rootLogo}>
                        <img src={logo} alt="Rnold home" />
                    </Link>
                </div>
                <div className={styles.gridItem2}>
                    <AuthControls />
                </div>
            </div>
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
                <div className={styles.adminDashboard}>
                    {user && user.role === ADMIN_ROLE && (
                        <NavLink
                            to="/admin"
                            className={({ isActive }) =>
                                isActive
                                    ? `${styles.navLink} ${styles.active}`
                                    : styles.navLink
                            }
                        >
                            Admin Dashboard
                        </NavLink>
                    )}
                </div>
            </div>
        </header>
    );
}
