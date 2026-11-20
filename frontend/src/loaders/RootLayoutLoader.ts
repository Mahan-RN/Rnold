import { type LoaderFunctionArgs } from "react-router";

import apiFetch from "../api/Fetch";

export interface CurrentUser {
    github_id: number;
    github_email: string;
    username: string;
    created_at: string;
    last_login: string;
    role: number;
}

export default async function rootLayoutLoader({
    request,
}: LoaderFunctionArgs) {
    const signal = request.signal;
    try {
        const user = await apiFetch<CurrentUser>("/users/me", {
            signal,
        });
        return user;
    } catch (error) {
        if (error instanceof Response && error.status === 401) {
            return null;
        } else {
            throw error;
        }
    }
}
