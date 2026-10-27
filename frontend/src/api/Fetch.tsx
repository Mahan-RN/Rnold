const BASE_URL = "/api";

export default async function apiFetch<T>(
    path: string,
    init: RequestInit = {}
): Promise<T> {
    const response = await fetch(`${BASE_URL}${path}`, init);
    if (!response.ok) {
        let message = response.statusText;

        try {
            const body = await response.json();
            if (typeof body.detail === "string") {
                message = body.detail;
            }
        } catch {
            // Keep the message as status text if the body isn't valid JSON
        }
        throw new Response(message, {
            status: response.status,
            statusText: response.statusText,
        });
    }
    if (response.status === 204) {
        return undefined as T;
    } else {
        return response.json() as Promise<T>;
    }
}
