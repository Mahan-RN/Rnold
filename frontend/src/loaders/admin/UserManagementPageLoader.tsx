import type { LoaderFunctionArgs } from "react-router";
import apiFetch from "src/api/Fetch";

export interface UserResponse {
    github_id: number;
    github_email: string;
    username: string;
    created_at: string;
    last_login: string;
    role: number;
}

export default async function userManagementPageLoader({
    request,
}: LoaderFunctionArgs) {
    const signal = request.signal;
    const userProfiles = await apiFetch<UserResponse[]>("/users", { signal });
    return userProfiles;
}
