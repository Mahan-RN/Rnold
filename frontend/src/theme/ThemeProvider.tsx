import type { ReactNode } from "react";
import { useEffect, useState } from "react";

import type { Theme } from "./themeContext";
import { ThemeContext } from "./themeContext";

function readInitialTheme(): Theme {
    // The inline script in index.html has already set this attribute.
    return document.documentElement.dataset.theme === "dark" ? "dark" : "light";
}

export function ThemeProvider({ children }: { children: ReactNode }) {
    const [theme, setTheme] = useState<Theme>(readInitialTheme);

    useEffect(() => {
        document.documentElement.dataset.theme = theme;
    }, [theme]);

    const toggle = () => {
        const next = theme === "light" ? "dark" : "light";
        setTheme(next);
        try {
            localStorage.setItem("theme", next);
        } catch {
            /* ignore */
        }
    };

    return (
        <ThemeContext.Provider value={{ theme, toggle }}>
            {children}
        </ThemeContext.Provider>
    );
}
