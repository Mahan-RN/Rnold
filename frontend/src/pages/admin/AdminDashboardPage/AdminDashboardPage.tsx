import { NavLink, Outlet } from "react-router";
import styles from "src/pages/admin/AdminDashboardPage/AdminDashboardPage.module.css";

export default function AdminDashboardPage() {
    return (
        <>
            <nav className={styles.navigationBar}>
                <NavLink
                    className={({ isActive }) =>
                        isActive
                            ? `${styles.navLink} ${styles.active}`
                            : styles.navLink
                    }
                    to="/admin/users"
                    end
                >
                    Users
                </NavLink>
                <NavLink
                    className={({ isActive }) =>
                        isActive
                            ? `${styles.navLink} ${styles.active}`
                            : styles.navLink
                    }
                    to="/admin/topics"
                    end
                >
                    Topics
                </NavLink>
            </nav>
            <Outlet />
        </>
    );
}
