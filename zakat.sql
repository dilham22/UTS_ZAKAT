-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 25 Mar 2025 pada 20.47
-- Versi server: 10.4.32-MariaDB
-- Versi PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `zakat`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `master_beras`
--

CREATE TABLE `master_beras` (
  `id` int(11) NOT NULL,
  `nama_beras` varchar(255) NOT NULL,
  `harga_per_kg` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `transaksi_zakat`
--

CREATE TABLE `transaksi_zakat` (
  `id` int(11) NOT NULL,
  `id_zakat` int(11) NOT NULL,
  `id_beras` int(11) NOT NULL,
  `jumlah_beras` int(11) NOT NULL,
  `total_harga` int(11) NOT NULL,
  `tanggal` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Struktur dari tabel `zakat_data`
--

CREATE TABLE `zakat_data` (
  `id` int(11) NOT NULL,
  `nama` varchar(255) NOT NULL,
  `jenis_zakat` varchar(255) NOT NULL,
  `jumlah` int(11) NOT NULL,
  `tanggal` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data untuk tabel `zakat_data`
--

INSERT INTO `zakat_data` (`id`, `nama`, `jenis_zakat`, `jumlah`, `tanggal`) VALUES
(14, 'tj', 'ksflkasjf', 2, '2025-03-29');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `master_beras`
--
ALTER TABLE `master_beras`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `transaksi_zakat`
--
ALTER TABLE `transaksi_zakat`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `zakat_data`
--
ALTER TABLE `zakat_data`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `master_beras`
--
ALTER TABLE `master_beras`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT untuk tabel `transaksi_zakat`
--
ALTER TABLE `transaksi_zakat`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT untuk tabel `zakat_data`
--
ALTER TABLE `zakat_data`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
