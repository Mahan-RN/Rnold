import { data, type LoaderFunctionArgs } from "react-router";
import apiFetch from "src/api/Fetch";

import type { CurrentUser } from "../RootLayoutLoader";

export default async function adminLoader({ request }: LoaderFunctionArgs) {
    const user = await apiFetch<CurrentUser>("/users/me", {
        signal: request.signal,
    });

    if (user.role !== 2) {
        throw data("You do not have permission to view this page", {
            status: 403,
        });
    }

    return user;
}
