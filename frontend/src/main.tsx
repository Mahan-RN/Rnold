import "./index.css";

import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { createBrowserRouter } from "react-router";
import { RouterProvider } from "react-router/dom";

import deleteUserAction from "./actions/admin/deleteUserAction";
import problemAction from "./actions/admin/problemAction";
import createTopicAction from "./actions/admin/topicAction";
import deleteMeAction from "./actions/deleteMeAction";
import logoutAction from "./actions/logoutAction";
import problemPageAction from "./actions/problemPageAction";
import AdminErrorBoundary from "./boundaries/AdminErrorBoundary/AdminErrorBoundary";
import RootLayout from "./layouts/RootLayout";
import adminLoader from "./loaders/admin/adminLoader";
import topicManagementPageLoader from "./loaders/admin/TopicManagementPageLoader";
import userManagementPageLoader from "./loaders/admin/UserManagementPageLoader";
import homePageLoader from "./loaders/HomePageLoader";
import logoutLoader from "./loaders/logoutLoader";
import problemPageLoader from "./loaders/ProblemPageLoader";
import profilePageLoader from "./loaders/ProfilePageLoader";
import rootLayoutLoader from "./loaders/RootLayoutLoader";
import AboutPage from "./pages/AboutPage/AboutPage";
import AdminDashboardPage from "./pages/admin/AdminDashboardPage/AdminDashboardPage";
import ProblemManagementPage from "./pages/admin/ProblemManagementPage/ProblemManagementPage";
import TopicManagementPage from "./pages/admin/TopicManagementPage/TopicManagementPage";
import UserManagementPage from "./pages/admin/UserManagementPage/UserManagementPage";
import HomePage from "./pages/HomePage/HomePage";
import NotFoundPage from "./pages/NotFoundPage/NotFoundPage";
import ProblemPage from "./pages/ProblemPage/ProblemPage";
import ProfilePage from "./pages/ProfilePage/ProfilePage";

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
                action: problemPageAction,
                errorElement: <NotFoundPage />,
            },
            {
                path: "/profile",
                element: <ProfilePage />,
                loader: profilePageLoader,
                errorElement: <NotFoundPage />,
            },
            {
                path: "/admin",
                element: <AdminDashboardPage />,
                loader: adminLoader,
                ErrorBoundary: AdminErrorBoundary,
                children: [
                    {
                        path: "/admin/users",
                        element: <UserManagementPage />,
                        loader: userManagementPageLoader,
                        action: deleteUserAction,
                    },
                    {
                        path: "/admin/topics",
                        element: <TopicManagementPage />,
                        loader: topicManagementPageLoader,
                        action: createTopicAction,
                    },
                    {
                        path: "/admin/problems",
                        element: <ProblemManagementPage />,
                        action: problemAction,
                    },
                ],
            },
        ],
    },
    {
        path: "/logout",
        action: logoutAction,
        loader: logoutLoader,
    },
    {
        path: "/delete-me",
        action: deleteMeAction,
        loader: logoutLoader,
    },
]);

createRoot(document.getElementById("root")!).render(
    <StrictMode>
        <RouterProvider router={router} />
    </StrictMode>,
);
