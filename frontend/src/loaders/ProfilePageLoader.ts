import type { LoaderFunctionArgs } from "react-router";
import apiFetch from "src/api/Fetch";

export interface ProfileResponse {
    github_id: number;
    github_email: string;
    username: string;
    created_at: string;
    last_login: string;
    role: number;
}

export default async function profilePageLoader({
    request,
}: LoaderFunctionArgs) {
    const signal = request.signal;
    const myProfile = await apiFetch<ProfileResponse>("/users/me", {
        signal,
    });
    return myProfile;
}
