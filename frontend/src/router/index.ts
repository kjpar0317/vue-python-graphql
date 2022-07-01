import { defineAsyncComponent } from "vue";

const dynamicImport = (path: string) =>
  defineAsyncComponent(() => import(`../views/${path}.vue`));

// const dynamicImport = (path) => import(`../views/${path}.vue`);

/** @type {import('vue-router').RouterOptions['routes']} */
export const routes = [
  {
    path: "/",
    name: "defaultLayout",
    component: () => import("@/components/template/DefaultTemplate.vue"),
    meta: { requiresAuth: true, name: "fade" },
    children: [
      {
        path: "/",
        name: "Home",
        component: dynamicImport("Home"),
      },
      {
        path: "/about",
        name: "About",
        component: dynamicImport("About"),
      },
      {
        path: "/subscription",
        name: "Subscription",
        component: dynamicImport("Subscription"),
      },
    ],
  },
  {
    path: "/",
    name: "emptyLayout",
    component: () => import("@/components/template/EmptyTemplate.vue"),
    meta: { requiresAuth: false, name: "fade" },
    children: [
      {
        path: "/login",
        name: "Login",
        component: dynamicImport("Login"),
      },
      {
        path: "/:path(.*)",
        name: "Error",
        component: () => dynamicImport("NotFound"),
      },
    ],
  },
];
