<h1>Pyrogram Auto Kick Bot with MongoDB</h1>

<p>This Pyrogram bot kicks members from groups and channels after a specified time (default 30 days), with customizable kick time through a bot command. Only group admins can use its commands, and it has a whitelist feature to exempt certain members.</p2>
<h2>Setup</h2>

<ol>
  <li>Clone this repository:<br>
    <code>git clone https://github.com/i-ryme/Kick-Bot.git</code></li>

  <li>Install the required Python packages:<br>
    <code>pip install -r requirements.txt</code></li>

  <li>Set the following environment variables with your Telegram bot API key and MongoDB connection string:<br>
    <code>BOT_TOKEN="your_bot_token_here"</code><br>
    <code>MONGO_URL="your_mongodb_url_here"</code></li>
</ol>

<h2>Usage</h2>

<ol>
  <li>Start the bot by running:<br>
    <code>python bot.py</code></li>

  <li>Add the bot to a group or channel as an administrator.</li>

  <li>Use the <code>/settime</code> command in a private chat with the bot to set the kick time. For example:<br>
    <code>/settime 86400</code><br>
    This would set the kick time to 86400 seconds (1 day).</li>

  <li>Use the <code>/addtowhitelist</code> command in a private chat with the bot to add a member to the whitelist. For example:<br>
    <code>/addtowhitelist 123456789</code><br>
    This would add the member with user ID 123456789 to the whitelist.</li>

  <li>Wait for new members to join the group or channel. After the specified kick time has elapsed, the bot will automatically kick the members who have not been whitelisted.</li>
</ol>

<h2>License</h2>

<p>This project is licensed under the MIT License - see the <a href="LICENSE">LICENSE</a> file for details.</p>
