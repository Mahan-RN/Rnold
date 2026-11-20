import styles from "src/theme/ThemeToggle/ThemeToggle.module.css";

import { useTheme } from "../themeContext";

export function ThemeToggle() {
    const { theme, toggle } = useTheme();
    const next = theme === "light" ? "dark" : "light";

    return (
        <button
            type="button"
            className={styles.themeToggle}
            onClick={toggle}
            aria-label={`Switch to ${next} theme`}
        >
            {next === "dark" ? "Dark" : "Light"}
        </button>
    );
}
