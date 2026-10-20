import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { createBrowserRouter } from "react-router";
import { RouterProvider } from "react-router/dom";
import "./index.css";
import HomePage from "./pages/HomePage";
import NotFoundPage from "./pages/NotFoundPage";
import ProblemPage from "./pages/ProblemPage";
import AboutPage from "./pages/AboutPage";
import homePageLoader from "./loaders/HomePageLoader";

const router = createBrowserRouter([
    {
        path: "/",
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
        errorElement: <NotFoundPage />,
    },
]);

createRoot(document.getElementById("root")!).render(
    <StrictMode>
        <RouterProvider router={router} />
    </StrictMode>
);
