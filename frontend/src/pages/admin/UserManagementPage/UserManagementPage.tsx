import { useLoaderData } from "react-router";
import UserCollapsible from "src/components/admin/UserCollapsible/UserCollapsible";
import type userManagementPageLoader from "src/loaders/admin/UserManagementPageLoader";
import styles from "src/pages/admin/UserManagementPage/UserManagementPage.module.css";

export default function UserManagementPage() {
    const userProfiles = useLoaderData<typeof userManagementPageLoader>();

    return (
        <div className={styles.flexContainer}>
            <h1>User Management</h1>
            <div>
                {userProfiles.map((userProfile) => (
                    <UserCollapsible {...userProfile} />
                ))}
            </div>
        </div>
    );
}
