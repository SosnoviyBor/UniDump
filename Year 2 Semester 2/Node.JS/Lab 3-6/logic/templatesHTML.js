export const login_menu = `
            <div class="menu-element " id="admin-login-menu">
                <div class="search-element" id="admin-text">Admin log-in:</div>
                <div id="admin-login" class="inp-text">
                    <div id="login-text">Login: </div>
                    <input class="search-book search-element" id="login" type="text"/>
                </div>
                <div id="admin-password" class="inp-text">
                    <div id="pword-text">Password: </div>
                    <input class="search-book search-element" id="pword" type="password"/>
                </div>
                <div id="helpful-b">
                    <input class="admin-login-button" id="login-button" type="button" value="Login" onclick="login()"/>
                </div>
            </div>`;

export const admin_panel = `
         <div class="admin-panel" id="admin-panel">
            <div class="panel-name">Admin Panel</div>
            <div class="panel-field">
                <div class="field-name" id="text-title">Title</div>
                <input class="admin-enter-field" id="inp-title" type="text"/>
            </div>
            <div class="panel-field">
                <div class="field-name" id="text-author">Author</div>
                <input class="admin-enter-field" id="inp-author" type="text"/>
            </div>
            <div class="panel-field">
                <div class="field-name" id="text-desc">Description</div>
                <input class="admin-enter-field" id="inp-desc" type="text"/>
            </div>
            <div class="panel-field">
                <div class="field-name" id="text-img">Image link</div>
                <input class="admin-enter-field" id="inp-img" type="text"/>
            </div>
            <div class="panel-field">
                <input class="admin-panel-button" id="submit-new" type="button" value="Add to database" onclick="addBook()"/>
            </div>
        </div>`;