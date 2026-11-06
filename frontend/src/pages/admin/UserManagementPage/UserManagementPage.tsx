import { useLoaderData, useActionData } from "react-router";
import type deleteUserAction from "src/actions/admin/deleteUserAction";
import UserCollapsible from "src/components/admin/UserCollapsible/UserCollapsible";
import type userManagementPageLoader from "src/loaders/admin/UserManagementPageLoader";
import styles from "src/pages/admin/UserManagementPage/UserManagementPage.module.css";

export default function UserManagementPage() {
    const userProfiles = useLoaderData<typeof userManagementPageLoader>();
    const actionData = useActionData<typeof deleteUserAction>(); // undefined if successful

    let actionAlertElement;
    if (!actionData) {
        actionAlertElement = <></>;
    } else if (actionData.success) {
        actionAlertElement = (
            <p className={styles.SuccessMessage}>User delete successfully</p>
        );
    } else {
        actionAlertElement = (
            <p className={styles.ErrorMessage}>Error: {actionData.message}</p>
        );
    }
    return (
        <div className={styles.flexContainer}>
            <h1>User Management</h1>
            {actionAlertElement}
            <div>
                {userProfiles.map((userProfile) => (
                    <UserCollapsible {...userProfile} />
                ))}
            </div>
        </div>
    );
}
