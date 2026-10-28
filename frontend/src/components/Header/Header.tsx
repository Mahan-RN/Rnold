import { Link, NavLink } from "react-router";
import logo from "src/assets/logo.svg";
import styles from "src/components/Header/Header.module.css";
import AuthControls from "../AuthControls/AuthControls";

export default function Header() {
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
                    <AuthControls />
                </div>
            </div>
        </header>
    );
}
