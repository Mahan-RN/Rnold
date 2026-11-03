import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { createBrowserRouter } from "react-router";
import { RouterProvider } from "react-router/dom";
import "./index.css";
import HomePage from "./pages/HomePage/HomePage";
import NotFoundPage from "./pages/NotFoundPage/NotFoundPage";
import ProblemPage from "./pages/ProblemPage/ProblemPage";
import AboutPage from "./pages/AboutPage/AboutPage";
import homePageLoader from "./loaders/HomePageLoader";
import rootLayoutLoader from "./loaders/RootLayoutLoader";
import RootLayout from "./layouts/RootLayout";
import logoutLoader from "./loaders/logoutLoader";
import logoutAction from "./actions/logoutAction";
import problemPageLoader from "./loaders/ProblemPageLoader";
import ProfilePage from "./pages/ProfilePage/ProfilePage";
import profilePageLoader from "./loaders/ProfilePageLoader";

const router = createBrowserRouter([
    {
        id: "root",
        path: "/",
        loader: rootLayoutLoader,
        element: <RootLayout />,
        children: [
            {
                index: true,
                element: <HomePage />,
                loader: homePageLoader,
                HydrateFallback: () => <p>Loading...</p>,
                errorElement: <NotFoundPage />,
            },
            {
                path: "/about",
                element: <AboutPage />,
                errorElement: <NotFoundPage />,
            },
            {
                path: "/problems/:problemID",
                element: <ProblemPage />,
                loader: problemPageLoader,
                errorElement: <NotFoundPage />,
            },
            {
                path: "/profile",
                element: <ProfilePage />,
                loader: profilePageLoader,
                errorElement: <NotFoundPage />,
            },
        ],
    },
    {
        path: "/logout",
        action: logoutAction,
        loader: logoutLoader,
    },
]);

createRoot(document.getElementById("root")!).render(
    <StrictMode>
        <RouterProvider router={router} />
    </StrictMode>,
);
