import { useLoaderData } from "react-router";
import UserCollapsible from "src/components/admin/UserCollapsible/UserCollapsible";
import type userManagementPageLoader from "src/loaders/admin/UserManagementPageLoader";

export default function UserManagementPage() {
    const userProfiles = useLoaderData<typeof userManagementPageLoader>();

    return (
        <div>
            <h1>User Management</h1>
            <div>
                {userProfiles.map((userProfile) => (
                    <UserCollapsible {...userProfile} />
                ))}
            </div>
        </div>
    );
}
