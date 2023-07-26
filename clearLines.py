def clear(lines_to_clear):
    for _ in range(lines_to_clear):
        # Move the cursor up one line
        print('\033[F', end='')
        # Clear the line
        print('\033[K', end='')


